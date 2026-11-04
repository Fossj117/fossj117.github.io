// ---- Watercolor toggle tile (mirrors THEMES in assets/header_sketch_watercolor.html) ----
// The toggle stays a midtone blue in both themes so it reads against either background.
const WC_MID = { paperMix: 0.35, inkDarken: 0.3, palette: ['#2a7ae2', '#4a8ae2', '#3f7fd0', '#4069B1', '#5a92d8'] };
const WC_THEMES = { light: WC_MID, dark: WC_MID };
const WC_INK_TARGET = '#1b3a75';
const WC_MASK_SIZE = 390;          // px; must match --wc-size on #dark-mode-toggle
const WC_MASK_ASPECT = 1697 / 1681; // ink_mask.png height / width

function wcMix(hexA, hexB, t) {
    const a = hexA.match(/\w\w/g).map(h => parseInt(h, 16));
    const b = hexB.match(/\w\w/g).map(h => parseInt(h, 16));
    return 'rgb(' + a.map((v, i) => Math.round(v + (b[i] - v) * t)).join(',') + ')';
}

function randomizeToggleTile(btn) {
    const theme = WC_THEMES[document.body.classList.contains('dark-mode') ? 'dark' : 'light'];
    const base = theme.palette[Math.floor(Math.random() * theme.palette.length)];
    const size = btn.offsetWidth || 30;
    const x = -Math.random() * (WC_MASK_SIZE - size);
    const y = -Math.random() * (WC_MASK_SIZE * WC_MASK_ASPECT - size);
    btn.style.setProperty('--wc-ink', wcMix(base, WC_INK_TARGET, theme.inkDarken));
    btn.style.setProperty('--wc-paper', wcMix(base, '#ffffff', theme.paperMix));
    btn.style.setProperty('--wc-pos', x.toFixed(0) + 'px ' + y.toFixed(0) + 'px');
}

document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('dark-mode-toggle');

    // Apply the stored theme on page load
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }

    // Give the toggle a random watercolor tile (crop + colour) for the current theme
    randomizeToggleTile(toggleButton);

    toggleButton.addEventListener('click', () => {
        // flip like a header tile; swap to a new crop/colour at the midpoint
        toggleButton.classList.remove('wc-flip');
        void toggleButton.offsetWidth;
        toggleButton.classList.add('wc-flip');
        document.body.classList.toggle('dark-mode');
        let theme = 'light';
        if (document.body.classList.contains('dark-mode')) {
            theme = 'dark';
        }
        localStorage.setItem('theme', theme);
        setTimeout(() => randomizeToggleTile(toggleButton), 250);
    });
});

document.getElementById('dark-mode-toggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    const theme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('theme', theme);
});
