library("shiny")

ui = fluidPage(
    titlePanel("Simple Histogram"),
    sidebarLayout(
        sidebarPanel(
            sliderInput("bins", "Number of bins:", min=5, max=50, value=20)
        ),
        mainPanel(plotOutput("histPlot"))
    )
) 

server = function(input, output) {
    output$histPlot = renderPlot({
        data = rnorm(500) 
        hist(data, breaks=input$bins, col="pink", border="white",
             main="Histogram of Random Data", xlab="Value")
    })
}

shinyApp(ui=ui, server=server)
