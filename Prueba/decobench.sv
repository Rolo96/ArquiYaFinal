`timescale 1ns / 1ps

module decobench;

	logic [31:0] InstrD, PCPlus8D, ResultW;
	logic CLK,RegWriteW,RESET;
	logic [3:0] WA3W;
	
	logic [31:0] RD1D, RD2D,ExtImmD;
	logic PCSrcD,RegWriteD,MemtoRegD,MemWriteD,BranchD,ALUSrcD,NoWriteD;
	logic [1:0] FlagWriteD;
	logic [2:0] ALUControlD;
	logic [3:0] Rd,CondD,WA3D, RA1D, RA2D,A1,A2;

    //Instante the DUT
    Deco DUT(
        .InstrD(InstrD),
        .PCPlus8D(PCPlus8D),
        .ResultW(ResultW), 
        .CLK(CLK),
        .RegWriteW(RegWriteW), 
        .RESET(RESET), 
        .WA3W(WA3W), 
        .RD1D(RD1D),
        .RD2D(RD2D), 
        .ExtImmD(ExtImmD), 
        .PCSrcD(PCSrcD), 
        .RegWriteD(RegWriteD), 
        .MemtoRegD(MemtoRegD), 
        .MemWriteD(MemWriteD),
        .BranchD(BranchD),
        .ALUSrcD(ALUSrcD),
        .NoWriteD(NoWriteD),
        .FlagWriteD(FlagWriteD),
        .ALUControlD(ALUControlD),
	.Rd(Rd), 
        .CondD(CondD),
        .WA3D(WA3D),
        .RA1D(RA1D),
        .RA2D(RA2D),
        .A1(A1),
        .A2(A2)
    );

    initial begin
        CLK = 1'b0;
        RESET=0'b1;	
	InstrD=32'b11100000000000010010000000000011;
	PCPlus8D=32'd4;
	ResultW=32'b11100000000000010010000000000000;
	RegWriteW=1'b1;
	WA3W=4'b0001;
	
        forever begin
            #5
            CLK = ~CLK;
        end
    end
    
    initial begin
        #25;
        RESET=0'b0;
	
        #1000;
        
        $stop;
    end
endmodule
