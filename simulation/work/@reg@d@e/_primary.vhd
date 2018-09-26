library verilog;
use verilog.vl_types.all;
entity RegDE is
    generic(
        BITS            : integer := 32
    );
    port(
        RD1D            : in     vl_logic_vector;
        RD2D            : in     vl_logic_vector;
        ExtImmD         : in     vl_logic_vector;
        PCSrcD          : in     vl_logic;
        RegWriteD       : in     vl_logic;
        MemtoRegD       : in     vl_logic;
        MemWriteD       : in     vl_logic;
        BranchD         : in     vl_logic;
        ALUSrcD         : in     vl_logic;
        CLR             : in     vl_logic;
        CLK             : in     vl_logic;
        NoWriteD        : in     vl_logic;
        FlagWriteD      : in     vl_logic_vector(1 downto 0);
        ALUControlD     : in     vl_logic_vector(2 downto 0);
        FlagsD          : in     vl_logic_vector(3 downto 0);
        CondD           : in     vl_logic_vector(3 downto 0);
        WA3D            : in     vl_logic_vector(3 downto 0);
        RD1E            : out    vl_logic_vector;
        RD2E            : out    vl_logic_vector;
        ExtImmE         : out    vl_logic_vector;
        PCSrcE          : out    vl_logic;
        RegWriteE       : out    vl_logic;
        MemtoRegE       : out    vl_logic;
        MemWriteE       : out    vl_logic;
        BranchE         : out    vl_logic;
        ALUSrcE         : out    vl_logic;
        FlagWriteE      : out    vl_logic;
        NoWriteE        : out    vl_logic;
        ALUControlE     : out    vl_logic_vector(2 downto 0);
        FlagsE          : out    vl_logic_vector(3 downto 0);
        CondE           : out    vl_logic_vector(3 downto 0);
        WA3E            : out    vl_logic_vector(3 downto 0)
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end RegDE;
