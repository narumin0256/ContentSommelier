document.getElementById('myForm').addEventListener('submit',
    function(event){
        event.preventDefault();
        // nameにformで受け取った値を渡す
        const name = document.getElementById('name').value;
        // idがresultのところに返す
        document.getElementById('result').textContent = `Hello, ${name}!`;
});