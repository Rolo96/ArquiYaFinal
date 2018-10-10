`timescale 1ns / 1ps

module Decoder #(parameter BITS = 32) (
	input logic [BITS-1:0] InstrD,
	output logic [1:0] Op,
	output logic [5:0] Funct,
	output logic [3:0] Rd,CondD,RA1D,RA2D,WA3D,
	output logic [24:0] ExtImmD);

	assign Op = InstrD[27:26];

	always_comb
		if(Op==2'b11) begin
			Funct = InstrD[30:25];
			Rd = InstrD[25:22];
			CondD = 4'b1110;
			RA1D = 4'b0;
			RA2D = 4'b0;
			WA3D = InstrD[25:22];
			ExtImmD = InstrD[23:0];
		end
		else begin
			Funct = InstrD[25:20];
			Rd = InstrD[15:12];
			CondD = InstrD[31:28];
			RA1D = InstrD[19:16];
			RA2D = InstrD[3:0];
			WA3D = InstrD[15:12];
			ExtImmD = InstrD[23:0];
		end
endmodule