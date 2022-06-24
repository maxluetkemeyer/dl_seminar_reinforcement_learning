import { createApp } from "vue";
import App from "./App.vue";

import ModelPlayer from "./components/ModelPlayer.vue";
import HumanPlayer from "./components/HumanPlayer.vue";
import GymEnv from "./components/GymEnv.vue";
import ActionRender from "./components/ActionRender.vue";

const app = createApp(App);

app.component("ModelPlayer", ModelPlayer);
app.component("HumanPlayer", HumanPlayer);
app.component("GymEnv", GymEnv);
app.component("ActionRender", ActionRender);

app.mount("#app");
