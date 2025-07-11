<script>
    import Router from "svelte-spa-router";
    import Login from "./pages/Login.svelte";
    import Main from "./pages/Main.svelte";
    import Signup from "./pages/Signup.svelte";
    import Write from "./pages/Write.svelte";
    import NotFound from "./pages/NotFound.svelte";
    import "./css/style.css";
    import {
        getAuth,
        GoogleAuthProvider,
        signInWithCredential,
    } from "firebase/auth";
    import { user$ } from "./store";
    import { onMount } from "svelte";
    import Loading from "./pages/Loading.svelte";
    import Mypage from "./pages/Mypage.svelte";


    let isLoading = true;

    const provider = new GoogleAuthProvider();
    provider.addScope("https://www.googleapis.com/auth/contacts.readonly"); // 쓰기 말고 읽기만

    const auth = getAuth();

    const checkLogin = async () => {
        const token = localStorage.getItem("token");
        if (!token) return (isLoading=false);
        const credential = GoogleAuthProvider.credential(null, token);
        const result = await signInWithCredential(auth, credential);
        const user = result.user;
        user$.set(user);
        isLoading=false;
    };

    const routes = {
        "/": Main,
        "/login": Login,
        "/signup": Signup,
        "/write": Write,
        "/mypage": Mypage,
        "*": NotFound,
    };
    onMount(()=>{
        checkLogin();
    })
</script>
{#if isLoading}
<Loading />
<!-- 가져올 때 앞에 $ 를 붙여줘야 값을 가져올 수 있다. -->
{:else if !$user$}
    <Login />
{:else}
    <Router {routes} />
{/if}
