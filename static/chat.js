function handleRequestMsg (e) {
    e.preventDefault();
    const input = document.querySelector("#chat-input");
    createMsg(input.value);
}

function handleDisplayMsg (value) {
    const ul = document.querySelector("#chat-ul");


    value.forEach((item)=>{
        const li = document.createElement("li");
        const time = document.createElement("span");
        li.textContent = item.msg;
        time.textContent = item.id;
        ul.appendChild(li);
        ul.appendChild(time);
    })

}

async function readMsg() {
    const res = await fetch("/chat");
    const res_json = await res.json();
    const ul = document.querySelector("#chat-ul");
    ul.textContent = "";

    handleDisplayMsg(res_json);
}

async function createMsg(value) {

    const 현재날짜 = new Date();
    const 년 = 현재날짜.getFullYear();
    const 월 = (현재날짜.getMonth()+1);
    const 일 = 현재날짜.getDate();
    const 시 = 현재날짜.getHours();
    const 분 = 현재날짜.getMinutes();

    const 보낸시간 = `${년}년 ${월}월 ${일}일 ${시}:${분}`;

    console.log(value);

    const res = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-type" : "application/json"
        },
        body: JSON.stringify({
            id: 보낸시간,
            msg: value
        })
    });

    readMsg();
}

const form = document.querySelector("#chat-form");
form.addEventListener("submit", handleRequestMsg);

readMsg();