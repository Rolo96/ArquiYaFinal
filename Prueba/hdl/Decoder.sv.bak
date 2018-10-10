`timescale 1ns / 1ps

module Decoder #(parameter BITS = 32) (
	input logic [BITS-1:0] InstrD,
	output logic [1:0] Op,
	output logic [5:0] Funct,
	output logic [3:0] Rd,CondD,RA1D,RA2D,WA3D,
	output logic [23:0] ExtImmD);

	assign Op = InstrD[27:26];
	assign Funct = InstrD[25:20];
	assign Rd = InstrD[15:12];
	assign CondD = InstrD[31:28];
	assign RA1D = InstrD[19:16];
	assign RA2D = InstrD[3:0];
	assign WA3D = InstrD[15:12];
	assign ExtImmD = InstrD[23:0];

endmodule