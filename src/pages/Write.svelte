<script>
    import { getDatabase, ref, push } from "firebase/database";
    import Nav from "../components/Nav.svelte";
    import { getStorage, ref as refImage, uploadBytes, getDownloadURL } from "firebase/storage";

    let title;
    let price;
    let description;
    let place;
    let files;

    const storage = getStorage();
    const db = getDatabase();

    function writeUserData(imgUrl) {
        const db = getDatabase();
        push(ref(db, "item/"), {
            title,
            price,
            description,
            place,
            imgUrl,
            insertAt: new Date().getTime(),
        });
        alert("글쓰기 완료");
        window.location.hash = "/";
    }

    const uploadFile = async () => {
        const file = files[0];
        const name = file.name;
        const imgRef = refImage(storage, name);
        await uploadBytes(imgRef, file);
        const url = await getDownloadURL(imgRef);
        console.log("응답", url);

        return url
    };

    const handleSubmit = async () => {  // url 를 받아올때까지 기다렸다가 받아오면 data 를 같이 등록
        const url = await uploadFile()
        writeUserData(url);
    };
</script>

<form id="write-form" on:submit|preventDefault={handleSubmit}>
    <div>
        <label for="image">이미지</label>
        <input type="file" id="image" name="image" bind:files={files} />
    </div>
    <div>
        <label for="title">제목</label>
        <input type="text" id="title" name="title" bind:value={title} />
    </div>
    <div>
        <label for="price">가격</label>
        <input type="number" id="price" name="price" bind:value={price} />
    </div>
    <div>
        <label for="description">설명</label>
        <input
            type="text"
            id="description"
            name="description"
            bind:value={description}
        />
    </div>
    <div>
        <label for="place">장소</label>
        <input type="text" id="place" name="place" bind:value={place} />
    </div>
    <button class="submit-btn" type="submit">등록</button>
</form>
<Nav location="write" />

<style>
    .submit-btn {
        background-color: orange;
        color: white;
        padding: 5px 8px;
        border-radius: 30%;
    }
</style>
