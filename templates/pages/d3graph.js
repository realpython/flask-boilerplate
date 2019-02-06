 
console.log(data.chart_data);

 var graphData = data.chart_data
    // Set the dimensions of the svg
    var margin = {top: 30, right: 50, bottom: 30, left: 50};
    var svgWidth = 600;
    var svgHeight = 270;
    var graphWidth = svgWidth - margin.left - margin.right;
    var graphHeight = svgHeight - margin.top - margin.bottom;
    // Parse the date / time
    var parseDate = d3.time.format("%Y-%m-%d").parse;
    // Set the ranges
    var x = d3.time.scale().range([0, graphWidth]);
    var y = d3.scale.linear().range([graphHeight, 0]);
    // Define the axes
    var xAxis = d3.svg.axis().scale(x)
        .orient("bottom").ticks(5);
    var yAxis = d3.svg.axis().scale(y)
        .orient("left").ticks(5);
    // Define the High line
    var highLine = d3.svg.line()
        .x(function(d) { return x(d.Date); })
        .y(function(d) { return y(d.High); });
    var closeLine = d3.svg.line()
        .x(function(d) { return x(d.Date); })
        .y(function(d) { return y(d.Close); });
    var lowLine = d3.svg.line()
        .x(function(d) { return x(d.Date); })
        .y(function(d) { return y(d.Low); });
    var area = d3.svg.area()
      .x(function(d) { return x(d.Date); })
      .y0(function(d) { return y(d.Low); })
      .y1(function(d) { return y(d.High); })
    // Adds the svg canvas
    var svg = d3.select("#graphDiv")
      .append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight)
      .append("g")
        .attr("transform", 
        "translate(" + margin.left + "," + margin.top + ")")
    // define function
    function draw(data) {
      data.forEach(function(d) {
        d.Date = parseDate(d.Date);
        d.High = +d.High;
        d.Close = +d.Close;
        d.Low = +d.Low;
      });
      // Scale the range of the data
      x.domain(d3.extent(data, function(d) { return d.Date; }));
      y.domain([d3.min(data, function(d) {
          return Math.min(d.High, d.Close, d.Low) }),
          d3.max(data, function(d) {
          return Math.max(d.High, d.Close, d.Low) })]);
      // Add the area path.
      svg.append("path")
        .datum(data)
        .attr("class", "area")
        .attr("d", area)
      // Add the 2 valueline paths.
      svg.append("path")
        .style("stroke", "green")
        .style("fill", "none")
        .attr("class", "line")
        .attr("d", highLine(data));
      svg.append("path")
        .style("stroke", "blue")
        .style("fill", "none")
        .style("stroke-dasharray", ("3, 3"))
        .attr("d", closeLine(data));
      svg.append("path")
        .style("stroke", "red")
        .attr("d", lowLine(data));
      // Add the X Axis
      svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + graphHeight + ")")
          .call(xAxis);
      // Add the Y Axis
      svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);
      svg.append("text")
        .attr("transform", "translate("+(graphWidth+3)+","+y(graphData[0].High)+")")
        .attr("dy", ".35em")
        .attr("text-anchor", "start")
        .style("fill", "green")
        .text("High");
      svg.append("text")
        .attr("transform", "translate("+(graphWidth+3)+","+y(graphData[0].Low)+")")
        .attr("dy", ".35em")
        .attr("text-anchor", "start")
        .style("fill", "red")
        .text("Low");
      svg.append("text")
        .attr("transform", "translate("+(graphWidth+3)+","+y(graphData[0].Close)+")")
        .attr("dy", ".35em")
        .attr("text-anchor", "start")
        .style("fill", "blue")
        .text("Close");
    };

	draw(graphData);