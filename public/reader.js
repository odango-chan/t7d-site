
(() => {
  const root = document.documentElement;
  const widths = { narrow: "34rem", normal: "42rem", wide: "52rem" };
  const state = {
    theme: localStorage.getItem("t7d-theme") || "light",
    scale: Number(localStorage.getItem("t7d-font-scale") || "1"),
    width: localStorage.getItem("t7d-reader-width") || "normal",
  };

  const apply = () => {
    root.dataset.theme = state.theme;
    root.style.setProperty("--font-scale", String(state.scale));
    root.style.setProperty("--reader-width", widths[state.width] || widths.normal);
  };
  apply();

  document.querySelector("[data-reader-theme]")?.addEventListener("click", () => {
    state.theme = state.theme === "light" ? "dark" : "light";
    localStorage.setItem("t7d-theme", state.theme);
    apply();
  });

  document.querySelector("[data-reader-font-down]")?.addEventListener("click", () => {
    state.scale = Math.max(.85, +(state.scale - .05).toFixed(2));
    localStorage.setItem("t7d-font-scale", String(state.scale));
    apply();
  });

  document.querySelector("[data-reader-font-up]")?.addEventListener("click", () => {
    state.scale = Math.min(1.3, +(state.scale + .05).toFixed(2));
    localStorage.setItem("t7d-font-scale", String(state.scale));
    apply();
  });

  document.querySelector("[data-reader-width]")?.addEventListener("click", () => {
    state.width = state.width === "normal" ? "wide" : state.width === "wide" ? "narrow" : "normal";
    localStorage.setItem("t7d-reader-width", state.width);
    apply();
  });

  const template = document.querySelector("#day1-inline-slot");
  const paragraphs = document.querySelectorAll(".prose p");
  if (template && paragraphs.length > 9) {
    paragraphs[9].after(template.content.cloneNode(true));
  }
})();
