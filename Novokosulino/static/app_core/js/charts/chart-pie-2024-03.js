// Set new default font family and font color to mimic Bootstrap's default styling
(Chart.defaults.global.defaultFontFamily = "Nunito"),
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#858796";

// Pie Chart Example
var ctx = document.getElementById("StearingCommittee-First-2024");
var Secretary = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["За", "Воздержались", "Против"],
    datasets: [
      {
        data: [567.55, 119, 37.04],
        backgroundColor: ["#1cc88a", "#dcde73", "#de7373"],
        hoverBackgroundColor: ["#018c59", "#adb002", "#e24646"],
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      },
    ],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: "#dddfeb",
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false,
    },
    cutoutPercentage: 50,
  },
});
