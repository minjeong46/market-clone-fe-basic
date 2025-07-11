// 프론트 저장소같은 느낌
import { writable } from "svelte/store";

export const user$ = writable(null); // 수정할 수 있는 그런 값

