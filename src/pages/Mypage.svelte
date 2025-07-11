<script>
    import Nav from "../components/Nav.svelte";
    import { user$ } from "../store";

    const logout = () => {
        user$.set(null);
        localStorage.removeItem('token');
    };
</script>

<div>나의 당근</div>
<button on:click={logout}>로그아웃</button>

<Nav location="mypage" />

<style>
    button {
        border: 1px solid #ccc;
        cursor: pointer;
    }
</style>