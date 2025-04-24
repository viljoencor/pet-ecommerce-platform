var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

app.UseSwagger();
app.UseSwaggerUI();

app.MapPost("/api/orders", (OrderRequest order) =>
{
    return Results.Created($"/api/orders/{Guid.NewGuid()}", order);
});

app.MapGet("/api/orders/{id}", (string id) =>
{
    return Results.Ok(new {
        orderId = id,
        status = "pending",
        totalAmount = 999.99,
        createdAt = DateTime.UtcNow
    });
});

app.Run();

record OrderRequest(string UserId, List<OrderItem> Items, string? Notes);
record OrderItem(string ProductId, int Quantity, double Price);
