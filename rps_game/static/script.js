document.addEventListener('DOMContentLoaded', function() {
    const choices = document.querySelectorAll('.choice');
    const userChoiceDisplay = document.getElementById('user-choice');
    const computerChoiceDisplay = document.getElementById('computer-choice');
    const resultMessage = document.getElementById('result-message');
    const winsDisplay = document.getElementById('wins');
    const lossesDisplay = document.getElementById('losses');
    const tiesDisplay = document.getElementById('ties');
    
    choices.forEach(choice => {
        choice.addEventListener('click', function() {
            const userChoice = this.id;
            playGame(userChoice);
        });
    });
    
    function playGame(userChoice) {
        // Show user's choice
        userChoiceDisplay.innerHTML = `
            <img src="https://cdn-icons-png.flaticon.com/512/3221/3221${getIconCode(userChoice)}.png" alt="${userChoice}">
            <p>${capitalizeFirstLetter(userChoice)}</p>
        `;
        
        // Show loading for computer choice
        computerChoiceDisplay.innerHTML = '<div class="loading">...</div>';
        resultMessage.textContent = '';
        resultMessage.className = '';
        
        // Send request to server
        fetch('/play', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ choice: userChoice }),
        })
        .then(response => response.json())
        .then(data => {
            // Update computer choice
            computerChoiceDisplay.innerHTML = `
                <img src="https://cdn-icons-png.flaticon.com/512/3221/3221${getIconCode(data.computer_choice)}.png" alt="${data.computer_choice}">
                <p>${capitalizeFirstLetter(data.computer_choice)}</p>
            `;
            
            // Update score
            winsDisplay.textContent = data.score.wins;
            lossesDisplay.textContent = data.score.losses;
            tiesDisplay.textContent = data.score.ties;
            
            // Show result
            resultMessage.textContent = getResultMessage(data.result);
            resultMessage.classList.add(data.result);
            
            // Add animation
            animateResult(data.result);
        });
    }
    
    function getIconCode(choice) {
        const codes = {
            'rock': '897',
            'paper': '912',
            'scissors': '906'
        };
        return codes[choice] || '';
    }
    
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
    
    function getResultMessage(result) {
        const messages = {
            'win': 'You Win!',
            'lose': 'You Lose!',
            'tie': "It's a Tie!"
        };
        return messages[result];
    }
    
    function animateResult(result) {
        const animationClass = result === 'win' ? 'bounce' : 
                            result === 'lose' ? 'shake' : 'pulse';
        
        userChoiceDisplay.classList.add(animationClass);
        computerChoiceDisplay.classList.add(animationClass);
        
        setTimeout(() => {
            userChoiceDisplay.classList.remove(animationClass);
            computerChoiceDisplay.classList.remove(animationClass);
        }, 1000);
    }
});
