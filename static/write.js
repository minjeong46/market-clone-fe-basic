const form = document.getElementById("write-form");

const handleSubmitForm = async (e) => {
    e.preventDefault();
    const res = await fetch("/item", {
        method: "POST",
        body: new FormData(form),
    })
};

form.addEventListener("submit", handleSubmitForm);
