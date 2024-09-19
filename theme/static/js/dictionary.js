// dictionary.js

document.addEventListener('DOMContentLoaded', function() {
    // Éléments du DOM
    const searchInput = document.getElementById('searchInput');
    const wordItems = document.querySelectorAll('.word-item');
    const alphabetFilters = document.querySelectorAll('.alphabet-filter');
    const wordDetailsButtons = document.querySelectorAll('.word-details');
    const popup = document.getElementById('wordDetailsPopup');
    const closePopup = document.getElementById('closePopup');
    const toggleButton = document.getElementById('toggleKeyboard');
    const keyboardContainer = document.getElementById('aglcKeyboard');

    // Fonctionnalité de recherche
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        wordItems.forEach(item => {
            const word = item.dataset.word;
            const languageCode = item.querySelector('.text-sm.text-gray-500').textContent.toLowerCase();
            item.style.display = word.includes(searchTerm) || languageCode.includes(searchTerm) ? '' : 'none';
        });
        updateStatistics();
    });

    // Filtre alphabétique
    alphabetFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const letter = this.textContent.toLowerCase();
            wordItems.forEach(item => {
                const word = item.dataset.word;
                item.style.display = word.startsWith(letter) ? '' : 'none';
            });
            updateStatistics();
        });
    });

    // Popup de détails des mots
    wordDetailsButtons.forEach(button => {
        button.addEventListener('click', function() {
            const wordId = this.dataset.wordId;
            // Ici, vous feriez normalement une requête AJAX pour obtenir les détails du mot
            // Pour cet exemple, nous utilisons des données factices
            document.getElementById('popupWord').textContent = 'Exemple de mot';
            document.getElementById('popupTranslation').textContent = 'Traduction d\'exemple';
            document.getElementById('popupImage').src = '/chemin/vers/image.jpg';
            document.getElementById('popupAudio').src = '/chemin/vers/audio.mp3';
            document.getElementById('popupExample').textContent = 'Voici un exemple d\'utilisation du mot.';
            popup.classList.remove('hidden');
        });
    });

    closePopup.addEventListener('click', function() {
        popup.classList.add('hidden');
    });

    // Fonctionnalité du clavier AGLC
    const aglcKeys = ['ɓ', 'ɗ', 'ǝ', 'ɛ', 'ƒ', 'ɣ', 'ɨ', 'ŋ', 'ɔ', 'ʃ', 'ʊ', 'ʋ', 'ʒ', 'θ'];

    function createKeyboard() {
        const keyboard = document.createElement('div');
        keyboard.className = 'bg-white rounded-lg shadow-lg p-4 max-w-xl mx-auto';
        
        const keyboardLayout = document.createElement('div');
        keyboardLayout.className = 'grid grid-cols-7 gap-2';
        
        aglcKeys.forEach(key => {
            const button = document.createElement('button');
            button.textContent = key;
            button.className = 'bg-gray-100 hover:bg-green-500 hover:text-white text-gray-800 font-bold py-2 px-4 rounded-lg transition duration-200 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50';
            button.onclick = () => insertChar(key);
            keyboardLayout.appendChild(button);
        });
        
        keyboard.appendChild(keyboardLayout);
        return keyboard;
    }

    function insertChar(char) {
        const cursorPos = searchInput.selectionStart;
        const textBefore = searchInput.value.substring(0, cursorPos);
        const textAfter = searchInput.value.substring(cursorPos);
        searchInput.value = textBefore + char + textAfter;
        searchInput.setSelectionRange(cursorPos + 1, cursorPos + 1);
        searchInput.focus();
    }

    function toggleKeyboard() {
        if (keyboardContainer.style.display === 'none' || keyboardContainer.style.display === '') {
            keyboardContainer.style.display = 'block';
            keyboardContainer.innerHTML = '';
            keyboardContainer.appendChild(createKeyboard());
            keyboardContainer.style.opacity = '0';
            setTimeout(() => {
                keyboardContainer.style.opacity = '1';
            }, 50);
        } else {
            keyboardContainer.style.opacity = '0';
            setTimeout(() => {
                keyboardContainer.style.display = 'none';
                keyboardContainer.innerHTML = '';
            }, 300);
        }
    }

    toggleButton.addEventListener('click', toggleKeyboard);

    // Fonction pour mettre à jour les statistiques
    function updateStatistics() {
        const visibleWords = document.querySelectorAll('.word-item:not([style*="display: none"])');
        const totalWordsElement = document.getElementById('totalWords');
        const totalTranslationsElement = document.getElementById('totalTranslations');
        const totalLanguagesElement = document.getElementById('totalLanguages');

        if (totalWordsElement) {
            totalWordsElement.textContent = visibleWords.length;
        }

        // Calcul du nombre de traductions et de langues uniques
        const languages = new Set();
        let translationsCount = 0;

        visibleWords.forEach(word => {
            const languageCode = word.querySelector('.text-sm.text-gray-500').textContent;
            languages.add(languageCode);
            // Supposons que chaque mot a au moins une traduction
            translationsCount++;
        });

        if (totalTranslationsElement) {
            totalTranslationsElement.textContent = translationsCount;
        }

        if (totalLanguagesElement) {
            totalLanguagesElement.textContent = languages.size;
        }
    }

    // Appel initial pour mettre à jour les statistiques
    updateStatistics();

    // Styles additionnels pour le clavier AGLC
    const styles = `
        #aglcKeyboard {
            transition: opacity 0.3s ease-in-out;
            position: absolute;
            z-index: 1000;
            width: 100%;
            max-width: 500px;
            left: 50%;
            transform: translateX(-50%);
        }
    `;

    const styleSheet = document.createElement("style");
    styleSheet.innerText = styles;
    document.head.appendChild(styleSheet);
});
