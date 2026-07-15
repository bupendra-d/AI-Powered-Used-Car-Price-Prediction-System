// Dynamic Brand -> Model Dropdown// 

const brandDropdown = document.getElementById("brand");
const modelDropdown = document.getElementById("model");

// Load Brand-Model Mapping
fetch("/static/brand_model.json")
    .then(response => response.json())
    .then(data => {

        // Populate Brand Dropdown
        Object.keys(data)
            .sort()
            .forEach(brand => {

                let option = document.createElement("option");

                option.value = brand;

                option.textContent = brand;

                brandDropdown.appendChild(option);

            });


        // When Brand Changes
        brandDropdown.addEventListener("change", function () {

            let selectedBrand = this.value;

            // Clear Previous Models
            modelDropdown.innerHTML =
                "<option value=''>Select Model</option>";

            if (selectedBrand === "")
                return;

            // Populate Models
            data[selectedBrand].forEach(model => {

                let option = document.createElement("option");

                option.value = model;

                option.textContent = model;

                modelDropdown.appendChild(option);

            });

        });

    });