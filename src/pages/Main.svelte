        <script>
    import { onMount } from "svelte";
            import Footer from "../components/Footer.svelte";
                        import { getDatabase, ref, onValue } from "firebase/database";

            let hour = new Date().getHours();
            let min = new Date().getMinutes();

            // 반응현 변수
            $: item = [];

const db = getDatabase();
const itemRef = ref(db, 'item/');


onMount(()=>{ // 화면이 렌더링 됐을 때 마다 유지하도록 
    onValue(itemRef, (snapshot) => { // itemRef 가 바뀔때마다 snapshot 을 새롭게 내려줌
  const data = snapshot.val();
  item = Object.values(data);
  console.log(Object.values(data)); // data 가 Object 니깐 Object 의 value 값을 가져옴
});
})

        </script>
        <!-- <div class="media-info-msg">화면 사이즈를 줄여주세요.</div> -->
        <header>
            <div class="info-bar">
                <div class="info-bar__time">{hour}:{min}</div>
                <div class="info-bar__icons">
                    <img src="assets/chart-bar.svg" alt="chart-bar">
                    <img src="assets/wifi.svg" alt="wifi">
                    <img src="assets/battery.svg" alt="battery">
                </div>
            </div>
            <div class="menu-bar">
                <div class="menu-bar__location">
                    <span>역삼1동</span>
                    <img src="assets/arrow-down.svg" alt="arrow-down">
                </div>
                <div class="menu-bar__icons">
                    <img src="assets/search.svg" alt="search">
                    <img src="assets/bar.svg" alt="menu-bar">
                    <img src="assets/alert.svg" alt="alert-bell">
                </div>
            </div>
        </header>
        <main>
            {#each item as item}
            <div class="item-list">
                <div class="item-list__img"></div>
                <div class="item-list__info">
                    <div class="item-list__info-title">{item.title}</div>
                    <div class="item-list__info-meta">{item.price}</div>
                    <div class="item-list__info-price">{item.place}</div>
                     <div class="">{item.description}</div>
                </div>
            </div>

            {/each}
            <a class="write-btn" href="#/write">+ 글쓰기</a>
        </main>
        <Footer location='home' />
