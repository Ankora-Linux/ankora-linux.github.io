document.addEventListener('DOMContentLoaded', () => {
    const langBtn = document.getElementById('lang-switch');
    let currentLang = localStorage.getItem('ankora_lang') || 'tr';

    const updateLanguage = (lang) => {
        document.querySelectorAll('[data-tr][data-en]').forEach(el => {
            el.innerHTML = el.getAttribute(`data-${lang}`);
        });

        // Handle placeholders if there are any
        document.querySelectorAll('[data-tr-placeholder][data-en-placeholder]').forEach(el => {
            el.setAttribute('placeholder', el.getAttribute(`data-${lang}-placeholder`));
        });

        // Update language indicator in switcher button
        if (langBtn) {
            const trIndicator = langBtn.querySelector('.lang-tr');
            const enIndicator = langBtn.querySelector('.lang-en');
            if (trIndicator && enIndicator) {
                if (lang === 'tr') {
                    trIndicator.classList.add('active');
                    enIndicator.classList.remove('active');
                } else {
                    trIndicator.classList.remove('active');
                    enIndicator.classList.add('active');
                }
            }
        }

        document.documentElement.lang = lang;
        localStorage.setItem('ankora_lang', lang);
    };

    if (langBtn) {
        langBtn.addEventListener('click', () => {
            currentLang = currentLang === 'tr' ? 'en' : 'tr';
            updateLanguage(currentLang);
        });
    }

    // Initialize with default/saved language
    updateLanguage(currentLang);
});
