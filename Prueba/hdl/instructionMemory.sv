`timescale 1ns / 1ps

module InstructionMemory(input logic [31:0] a,
output logic [31:0] rd);
logic [31:0] RAM[0:31]; 
initial
$readmemb("Code.RS",RAM);
assign rd = RAM[a[31:2]]; 
endmodule