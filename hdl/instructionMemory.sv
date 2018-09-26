`timescale 1ns / 1ps

module InstructionMemory(input logic [31:0] a,
output logic [31:0] rd);
logic [31:0] RAM[63:0]; //Sustituir el 63 por numero de instrucciones - 1
initial
$readmemh("code.rs",RAM);
assign rd = RAM[a[31:2]]; 
endmodule