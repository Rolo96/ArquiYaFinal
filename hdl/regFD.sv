`timescale 1ns / 1ps

module RegFD #(parameter SIZE = 32)(
    input logic CLK, StallD,CLR,
    input logic [SIZE-1:0] InstrF,
    output logic [SIZE-1:0] InstrD
);

logic [SIZE-1:0] InstrD_temp;

always_ff@(posedge CLK)
begin
	if(StallD == 1'b0)
		if(CLR)
			InstrD_temp = {SIZE{1'b0}};
		else
			InstrD_temp = InstrF;
	else 
		InstrD_temp = InstrD_temp;
end

assign InstrD = InstrD_temp;

endmodule