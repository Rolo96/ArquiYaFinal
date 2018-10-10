`timescale 1ns / 1ps

module DataMemory(
	input logic CLK, WE,
	input logic [31:0] A, WD,
	output logic [31:0] RD);

	logic [31:0] RAM[1:0];

	//initial begin
		//$readmemb("C:\\Users\\Bryan\\Desktop\\MicroArqui\\ArquiYaFinal\\hdl\\Data_Image.di",RAM);
	//end

	assign RD = RAM[A[31:2]];

	always_ff @(negedge CLK)
	begin
		if (WE) RAM[A[31:2]] <= WD;
	end

endmodule