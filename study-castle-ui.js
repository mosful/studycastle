(function () {
    "use strict";

    const iconLabels = new Map([
        ["✕", "關閉"],
        ["×", "關閉"],
        ["🏠", "回首頁"],
        ["🌓", "切換顯示模式"],
        ["🔊", "播放音效"],
        ["🔇", "關閉音效"],
        ["⬆", "回到頁面頂端"],
        ["↑", "回到頁面頂端"]
    ]);

    function selectIncludingRoot(root, selector) {
        const elements = Array.from(root.querySelectorAll(selector));
        if (root instanceof Element && root.matches(selector)) {
            elements.unshift(root);
        }
        return elements;
    }

    function prepareMainContent() {
        let main = document.querySelector("main, [role='main']");
        if (!main) {
            main = document.querySelector(".app, .container, .content-wrap, .screen");
            if (main) {
                main.setAttribute("role", "main");
            }
        }
        if (!main) {
            return;
        }
        main.id ||= "main-content";
        if (!document.querySelector(".skip-link")) {
            const skipLink = document.createElement("a");
            skipLink.className = "skip-link";
            skipLink.href = `#${main.id}`;
            skipLink.textContent = "跳到主要內容";
            document.body.prepend(skipLink);
        }
    }

    function improveInteractiveElements(root = document) {
        selectIncludingRoot(root, "button").forEach((button) => {
            if (!button.hasAttribute("type")) {
                button.type = "button";
            }
            if (!button.getAttribute("aria-label")) {
                const text = button.textContent.replace(/\s+/g, " ").trim();
                const mappedLabel = iconLabels.get(text);
                if (mappedLabel) {
                    button.setAttribute("aria-label", mappedLabel);
                }
            }
        });

        selectIncludingRoot(root, "[onclick]:not(button):not(a):not(input):not(select):not(textarea)").forEach((element) => {
            element.setAttribute("role", "button");
            element.tabIndex = element.tabIndex >= 0 ? element.tabIndex : 0;
            if (element.dataset.keyboardReady === "true") {
                return;
            }
            element.dataset.keyboardReady = "true";
            element.addEventListener("keydown", (event) => {
                if (event.key === "Enter" || event.key === " ") {
                    event.preventDefault();
                    element.click();
                }
            });
        });

        selectIncludingRoot(root, "input, select, textarea").forEach((control) => {
            if (control.getAttribute("aria-label") || control.labels?.length) {
                return;
            }
            const fallbackLabel = control.getAttribute("placeholder")
                || control.getAttribute("title")
                || (control.tagName === "SELECT" ? "選擇項目" : "輸入內容");
            control.setAttribute("aria-label", fallbackLabel.replace(/\.{3}/g, "…"));
        });
    }

    function improveFeedbackAndDialogs(root = document) {
        selectIncludingRoot(root, ".feedback, .feedback-box, [id*='feedback'], [id*='result']").forEach((element) => {
            element.setAttribute("aria-live", "polite");
            element.setAttribute("aria-atomic", "true");
        });

        selectIncludingRoot(root, ".modal-overlay, .wb-modal-overlay, .castle-modal-overlay").forEach((overlay) => {
            const dialog = overlay.querySelector(".modal-box, .wb-modal, .castle-modal-box") || overlay.firstElementChild;
            if (dialog) {
                dialog.setAttribute("role", "dialog");
                dialog.setAttribute("aria-modal", "true");
            }
        });
    }

    function improveImages(root = document) {
        selectIncludingRoot(root, "img").forEach((image, index) => {
            if (!image.hasAttribute("alt")) {
                image.alt = "";
            }
            if (!image.hasAttribute("loading") && index > 0) {
                image.loading = "lazy";
            }
        });
    }

    function initialize() {
        prepareMainContent();
        improveInteractiveElements();
        improveFeedbackAndDialogs();
        improveImages();

        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                mutation.addedNodes.forEach((node) => {
                    if (!(node instanceof Element)) {
                        return;
                    }
                    improveInteractiveElements(node);
                    improveFeedbackAndDialogs(node);
                    improveImages(node);
                });
            });
        });
        observer.observe(document.body, { childList: true, subtree: true });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initialize, { once: true });
    } else {
        initialize();
    }
}());
