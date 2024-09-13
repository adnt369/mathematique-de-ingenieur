document.getElementById('form-coordonnees').addEventListener('submit', function(event) {
    event.preventDefault(); // Empêche le rechargement de la page lors de la soumission

    // Récupérer les valeurs du formulaire
    let nom = document.getElementById('nom').value;
    let prenom = document.getElementById('prenom').value;
    let email = document.getElementById('email').value;
    let telephone = document.getElementById('telephone').value;
    let adresse = document.getElementById('adresse').value;

    // Afficher un message de confirmation
    let message = `Merci ${prenom} ${nom}, vos coordonnées ont été enregistrées.`;
    document.getElementById('message').textContent = message;

    // Vous pouvez envoyer les données à un serveur ici en utilisant fetch() ou AJAX
});
