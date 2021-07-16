timer = document.getElementsByClassName("timer")[0];

due_date = new Date("23 July, 2021 00:00:00");

pad_zero = function (number, target_length) {
  padded = number.toString();
  while (padded.length < target_length) {
    padded = "0" + padded;
  }
  return padded;
};

update_timer = function () {
  now = Date.now();
  delta = due_date - now;

  seconds = Math.floor(delta / 1000);
  minutes = Math.floor(seconds / 60);
  hours = Math.floor(minutes / 60);
  days = Math.floor(hours / 24);

  timer.innerHTML = `${days} days, ${pad_zero(hours % 24, 2)}:${pad_zero(
    minutes % 60,
    2
  )}:${pad_zero(seconds % 60, 2)}`;
};

setInterval(update_timer, 500);
