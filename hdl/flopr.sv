`timescale 1ns / 1ps

module Flopr #(parameter WIDTH = 8)
(input logic CLK, RESET,ENABLED,
input logic [WIDTH-1:0] d,
output logic [WIDTH-1:0] q);
always_ff @(posedge CLK, posedge RESET)
if (RESET) q <= 0;
else if(ENABLED) q <= d;
endmodule