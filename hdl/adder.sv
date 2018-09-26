module adder #(parameter WIDTH = 8)
(input logic [WIDTH-1:0] a, b,
output logic [WIDTH-1:0] PCPlus4F);
assign PCPlus4F = a + b;
endmodule