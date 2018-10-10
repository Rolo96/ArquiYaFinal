library verilog;
use verilog.vl_types.all;
entity ControlUnit is
    port(
        Op              : in     vl_logic_vector(1 downto 0);
        Funct           : in     vl_logic_vector(5 downto 0);
        Rd              : in     vl_logic_vector(3 downto 0);
        FlagW           : out    vl_logic_vector(1 downto 0);
        PCS             : out    vl_logic;
        RegW            : out    vl_logic;
        MemW            : out    vl_logic;
        MemtoReg        : out    vl_logic;
        ALUSrc          : out    vl_logic;
        Branch          : out    vl_logic;
        ImmSrc          : out    vl_logic_vector(1 downto 0);
        RegSrc          : out    vl_logic_vector(1 downto 0);
        ALUControl      : out    vl_logic_vector(3 downto 0);
        NoWrite         : out    vl_logic
    );
end ControlUnit;
