document.addEventListener("click", (e) => {
  const dropdownBtn = e.target.closest(".dropdown-btn");

  if (dropdownBtn) {
    const dropdown = dropdownBtn.closest(".dropdown");
    const isAlreadyActive = dropdown.classList.contains("active");

    hideDropElements();
    if (isAlreadyActive) {
      dropdown.classList.remove("active");
      return;
    }

    dropdown.classList.add("active");
  } else {
    hideDropElements();
  }

  function hideDropElements() {
    const dropElements = document.querySelectorAll(".dropdown, .dropright");
    for (let element of dropElements) {
      element.classList.remove("active");
    }
  }
});

document.addEventListener("mouseover", (e) => {
  const dropright = e.target.closest(".dropright");
  const button = e.target.closest(".dropdown-content button");
  if (button) {
    hideDroprightElements();
  }
  if (dropright) {
    dropright.classList.add("active");
  }

  function hideDroprightElements() {
    const dropElements = document.querySelectorAll(".dropright");
    for (let element of dropElements) {
      element.classList.remove("active");
    }
  }
});
