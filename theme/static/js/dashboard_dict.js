alert('test')
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM chargé');
    console.log('Données globales:', globalData);

    // Fonction utilitaire pour vérifier si les données sont vides
    function isDataEmpty(data) {
        return !data || data.length === 0;
    }

    // Graphique Mots vs Traductions
    var ctx1 = document.getElementById('wordsVsTranslationsChart').getContext('2d');
    var motsParMois = globalData.motsParMois;
    var traductionsParMois = globalData.traductionsParMois;

    console.log('Données Mots vs Traductions:', motsParMois, traductionsParMois);

    if (isDataEmpty(motsParMois) && isDataEmpty(traductionsParMois)) {
        ctx1.font = '20px Arial';
        ctx1.fillText('Pas de données disponibles', 10, 50);
    } else {
        new Chart(ctx1, {
            type: 'line',
            data: {
                labels: motsParMois.map(item => `Mois -${item.month}`),
                datasets: [{
                    label: 'Mots',
                    data: motsParMois.map(item => item.count),
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }, {
                    label: 'Traductions',
                    data: traductionsParMois.map(item => item.count),
                    borderColor: 'rgb(255, 99, 132)',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Évolution des Mots et Traductions'
                    }
                }
            }
        });
    }

    // Graphique Traductions par Langue
    var ctx2 = document.getElementById('translationsPerLanguageChart').getContext('2d');
    var traductionsParLangue = globalData.traductionsParLangue;

    console.log('Données Traductions par Langue:', traductionsParLangue);

    if (isDataEmpty(traductionsParLangue)) {
        ctx2.font = '20px Arial';
        ctx2.fillText('Pas de données disponibles', 10, 50);
    } else {
        new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: traductionsParLangue.map(item => item.nom),
                datasets: [{
                    label: 'Nombre de traductions',
                    data: traductionsParLangue.map(item => item.traductions_count),
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Nombre de traductions par langue'
                    }
                }
            }
        });
    }

    // Graphique "Types" de Mots
    var ctx3 = document.getElementById('wordTypesChart').getContext('2d');
    var typesDeMots = globalData.typesDeMots;

    console.log('Données Types de Mots:', typesDeMots);

    if (isDataEmpty(typesDeMots)) {
        ctx3.font = '20px Arial';
        ctx3.fillText('Pas de données disponibles', 10, 50);
    } else {
        new Chart(ctx3, {
            type: 'pie',
            data: {
                labels: typesDeMots.map(item => item.first_letter),
                datasets: [{
                    data: typesDeMots.map(item => item.count),
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Répartition des mots par première lettre'
                    }
                }
            }
        });
    }
});