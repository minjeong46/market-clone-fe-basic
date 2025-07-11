<script>
    import {
        getAuth,
        signInWithPopup,
        GoogleAuthProvider,
    } from "firebase/auth";
    import { user$ } from "../store";
    import Nav from "../components/Nav.svelte";

    const provider = new GoogleAuthProvider();
    const auth = getAuth();
    const loginWithGoogle = async () => {
        try {
            const result = await signInWithPopup(auth, provider);
            const credential = GoogleAuthProvider.credentialFromResult(result);
            const token = credential.accessToken;
            const user = result.user;
            user$.set(user);
            localStorage.setItem('token', token);
        } catch (e) {
            console.error(e);
        }
    };
</script>

<div>
    {#if $user$}
        <div>{$user$?.displayName}님 환영합니다.</div>
    {/if}
    <div>로그인하기</div>
    <button class="login-btn" on:click={loginWithGoogle}>
        <img
            class="google-img"
            src="https://e7.pngegg.com/pngimages/326/85/png-clipart-google-logo-google-text-trademark.png"
            alt=""
        />
        <span>Google로 로그인하기</span>
    </button>
</div>
<Nav location='login'></Nav>

<!-- <form id="login-form" action="/signup" method="post">
    <div>로그인</div>
    <div>
        <label for="id">아이디 : </label>
        <input type="text" id="id" name="id" required />
    </div>
    <div>
        <label for="password">패스워드 : </label>
        <input type="password" id="password" name="password" required />
    </div>
    <div>
        <button type="submit">로그인</button>
    </div>
    <div id="info"></div>
</form> -->

<style>
    .login-btn {
        width: 200px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        border: 1px solid #ccc;
        border-radius: 3px;
    }
    .google-img {
        width: 20px;
    }
</style>
