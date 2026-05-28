async function convert() {
    const value = document.getElementById("value").value;
    const conversionType = document.getElementById("conversionType").value;

    if (!value) {
        alert("Please enter a value!");
        return;
    }

    const response = await fetch(`/convert/${conversionType}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value: value })
    });

    const data = await response.json();
    document.getElementById("result").innerText =
        `Converted Value: ${data.converted_value} ${data.unit}`;
}
