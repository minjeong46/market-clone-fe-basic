import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";
import { getAuth } from "firebase/auth";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  apiKey: "AIzaSyAHCyqTmDhPTWSh6hsAOFwdOYA2Koy8J1Y",
  authDomain: "carrot-market-6b650.firebaseapp.com",
  databaseURL: "https://carrot-market-6b650-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "carrot-market-6b650",
  storageBucket: "carrot-market-6b650.firebasestorage.app",
  messagingSenderId: "887410188331",
  appId: "1:887410188331:web:c8945937bd61e0a7970a6e"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);
const storage = getStorage(app);
const auth = getAuth(app);

