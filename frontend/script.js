const SERVER_IP = 'http://127.0.0.1:8000'
$(document).ready(function() {
  // Add default option to dropdown
  var dropdown = $('#dropdown');
  dropdown.append($('<option></option>').attr('value', '').text('Select a state'));

  // Fetch state IDs from server and populate dropdown options
  $.ajax({
    url: SERVER_IP,
    type: 'GET',
    crossDomain: true,
    success: function(response) {
      // Clear existing options
      dropdown.find('option:not(:first-child)').remove();
      // Add new options
      $.each(response.stateIds, function(index, value) {
        dropdown.append($('<option></option>').attr('value', value).text(value));
      });
    },
    error: function(error) {
      alert(error);
    }
  });

  // Set default date in calendar input
  var today = new Date().toLocaleDateString('fr-CA', {year:'numeric', month: '2-digit', day:'2-digit'});
  $('#calendar').val(today);

  var city;
  var state;

  // Validate user input and format city name
  function city_state_entered() {
    city = $('#city-input').val().trim();
    state = $('#dropdown').val();

    if(city.length == 0 || city == 'Enter the city name') {
      alert('Please enter a city name');
      return false;
    }

    // Validate city name contains only English letters and spaces
    var RegExpression = /^[a-zA-Z\s]+$/;
    if(!RegExpression.test(city)) {
      alert('Only English letters allowed');
      city = $('#city-input').val('');
      return false;
    }

    if(state.length == 0 || state == 'Select a state') {
      alert('Please choose a state');
      return false;
    }

    // Format city name: convert rest of the letters to lowercase and capitalize first letter of each word
    city = city.toLowerCase();
    city = city.replace(/\b\w/g, (char) => char.toUpperCase());
    $('#city-input').val(city);

    return true;
  }

  // Clear default text when user clicks on city input
  $('#city-input').click(function() {$(this).val('');});

  // Handle search button click
  $('#search-city').click(function() {
    if(!city_state_entered()) return;
    $('#lat').val('');
    $('#lon').val('');
    $('#tz').val('');

    // Fetch latitude, longitude, and timezone from server
    $.ajax({
      url: SERVER_IP + '/coordinate',
      type: 'GET',
      crossDomain: true,
      data:{
        'city_name' : city,
        'state_id' : state
      },
      success: function(response) {
        $('#lat').val(response.lat);
        $('#lon').val(response.lon);
        $('#tz').val(response.tz);
      },
      error: function(error) {
        alert(error.responseJSON.error);
      }
    });
  });

  // Update slider value display
  $('.slider').on('input', function() {
    $(this).next().val($(this).val());
  });

  // Handle efficiency calculation button click
  $('#compute-effi').click(function(){
    if(!city_state_entered()) return;

    // Fetch efficiency data from server and display using D3.js
    $.ajax({
      url: SERVER_IP + '/efficiency',
      type: 'GET',
      crossDomain: true,
      data:{
        'lat': $('#lat').val(),
        'lon': $('#lon').val(),
        'timezone': $('#tz').val(),
        'start': $('#calendar').val(),
        'absorb_rate': $('#absorb-rate').val(),
        'panel_angle': $('#panel-angle').val(),
        'pipe_efficiency': $('#pipe-efficiency').val()
      },
      success: function(response) {
        // Load the visualization
        linechart(response);
      },
      error: function(error) {
        alert(error.responseJSON.error);
      }
    });
  });
});
