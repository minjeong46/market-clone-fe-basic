<script>
    import { getDatabase, ref, push } from "firebase/database";
    import Footer from "../components/Footer.svelte";

    let title
    let price
    let description
    let place

    function writeUserData() {
        const db = getDatabase();
        push(ref(db, 'item/'), {
            title,
            price,
            description,
            place
        });
        alert('글쓰기 완료')
        window.location.hash = "/";
    }
</script>

<!-- <button on:click={()=>console.log(title, price, description, place)}>테스트</button> -->
<form id="write-form" on:submit|preventDefault={writeUserData}>
            <!-- <div>
                <label for="image">이미지</label>
                <input type="file" id="image" name="image" />
            </div> -->
            <div>
                <label for="title">제목</label>
                <input type="text" id="title" name="title" bind:value={title}>
            </div>
            <div>
                <label for="price">가격</label>
                <input type="number" id="price" name="price"  bind:value={price} />
            </div>
            <div>
                <label for="description">설명</label>
                <input type="text" id="description" name="description"  bind:value={description} />
            </div>
            <div>
                <label for="place">장소</label>
                <input type="text" id="place" name="place"  bind:value={place} />
            </div>
            <button class="submit-btn" type="submit">등록</button>
        </form>
        <Footer location="write"/>

        <style>
            .submit-btn {
                background-color: orange;
                color: white;
                padding: 5px 8px;
                border-radius: 30%;
            }
        </style>