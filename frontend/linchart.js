function linechart(response) {
    // When the document is ready, execute this function
    $(document).ready(function() {
      // Configuration settings for the chart size and margins
      const config_size = {
        svg_width: 800,
        svg_height: 400,
        plot_margin: {
          left: 30,
          right: 20,
          top: 20,
          bottom: 20,
        },
      };
  
      // Remove any existing SVG element and add a new one to the #chart element
      d3.select('#chart').select('svg').remove();
      const svg = d3.select('#chart').append('svg')
        .attr('width', config_size.svg_width)
        .attr('height', config_size.svg_height)
        .attr('id', 'linechart');
  
      // Map the response data to an array of objects with hour and count properties
      const data = Object.keys(response).map(key => ({
        hour: new Date(key).getHours(),
        cnt: response[key],
      }));
  
      // Add a group element for the plot and set its position
        city = $('#city-input').val();
        date = $('#calendar').val()
      const plot_g = svg.append('g').classed('plot', true)
        .attr('transform', `translate(${config_size.plot_margin.left}, ${config_size.plot_margin.top})`);
      var title = svg.append("g")
        .attr("class", "title")
        .attr("transform", "translate(" + (config_size.svg_width / 2) + ", " + (config_size.plot_margin.top) + ")");
        title.append("text")
        .attr("x", 0)
        .attr("y", 0)
        .attr("id", "tittle")
        .attr("text-anchor", "middle")
        .style("font-size", "20px")
        .text("Hourly heater efficiency for " + city + " on " + date);
  
      // Set the plot width and height based on the configuration settings
      const plot_width = config_size.svg_width - config_size.plot_margin.left - config_size.plot_margin.right;
      const plot_height = config_size.svg_height - config_size.plot_margin.top - config_size.plot_margin.bottom;
  
      // Add a background rectangle to the plot
      const background = plot_g.append('rect')
        .attr('width', plot_width)
        .attr('height', plot_height)
        .attr('fill', 'blue')
        .attr('fill-opacity', 0.00);
  
      // Create a linear scale for the x-axis
      const x = d3.scaleLinear()
        .domain(d3.extent(data, d => d.hour))
        .range([0, plot_width]);
  
      // Add the x-axis to the plot
      plot_g.append('g')
        .attr('transform', `translate(${0},${plot_height - 5})`)
        .call(d3.axisBottom(x).tickFormat(d3.format('d')));
  
      // Create a linear scale for the y-axis
      const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.cnt)])
        .range([plot_height, 0]);
  
      // Add the y-axis to the plot
      plot_g.append('g')
        .attr('transform', `translate(${0},${0})`)
        .call(d3.axisLeft(y));
  
      // Add a line representing the data to the plot
      plot_g.append('path')
        .datum(data)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-width', 1.5)
        .attr('d', d3.line()
          .x(function(d) { return x(d.hour) })
          .y(function(d) { return y(d.cnt) })
        );
  
      // Add a group element for the mouse cursor and set its display to none
      const mouse_g = plot_g.append('g').classed('mouse', true).style('display', 'none');
  
      // Add a vertical line to the mouse cursor element
      mouse_g.append('rect')
        .attr('width', 2)
        .attr('x', -1)
        .attr('height', plot_height)
        .attr('fill', 'lightgray');

        mouse_g.append('circle').attr('r', 3).attr("stroke", "steelblue");
        mouse_g.append('text').attr('id', 'mark');

        plot_g.on("mouseover", function(mouse) {
            mouse_g.style('display', 'block');
        });
        const [min_hour, max_hour] = d3.extent(data, d=>d.hour);
        plot_g.on("mousemove", function(mouse) {
            const [x_cord,y_cord] = d3.pointer(mouse);
            const ratio = x_cord / plot_width;
            const current_hour = min_hour + Math.round(ratio * (max_hour - min_hour));
            if(current_hour < 0) return;
            const cnt = data.find(d => d.hour === current_hour).cnt;
            mouse_g.attr('transform', `translate(${x(current_hour)},${0})`);
            mouse_g.select('#mark').text(`hour: ${current_hour}, ${(cnt * 100).toFixed(2)} % efficiency`)
            .attr('text-anchor', current_hour < (min_hour + max_hour) / 2 ? "start" : "end").attr("y", (config_size.svg_height / 2));
            mouse_g.select('circle').attr('cy', y(cnt));
        });
        plot_g.on("mouseout", function(mouse) {
            mouse_g.style('display', 'none');
        });
    
    });
}