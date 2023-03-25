
document.getElementById("startTimer").addEventListener('click', function() {
    const count = document.getElementById("countdownTimer")
    let seconds = 60
    setInterval(updateTimer, 1000)
    function updateTimer() {
        seconds = seconds < 10 ? '0' + seconds : seconds
        if (seconds < 1) {
            count.innerHTML = '00'
            document.getElementById("timeLeft").value = "0"
            document.getElementById("typedForm").submit();
        }
        else {
            count.innerHTML = seconds
            seconds--
            document.getElementById("timeLeft").value = seconds
        }      
    };
})




