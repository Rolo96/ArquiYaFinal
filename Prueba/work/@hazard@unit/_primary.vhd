library verilog;
use verilog.vl_types.all;
entity HazardUnit is
    port(
        RegWriteM       : in     vl_logic;
        RegWriteW       : in     vl_logic;
        MemToRegE       : in     vl_logic;
        BranchTakenE    : in     vl_logic;
        PCSrcD          : in     vl_logic;
        PCSrcE          : in     vl_logic;
        PCSrcM          : in     vl_logic;
        PCSrcW          : in     vl_logic;
        Reset           : in     vl_logic;
        RA1D            : in     vl_logic_vector(3 downto 0);
        RA2D            : in     vl_logic_vector(3 downto 0);
        RA1E            : in     vl_logic_vector(3 downto 0);
        RA2E            : in     vl_logic_vector(3 downto 0);
        WA3M            : in     vl_logic_vector(3 downto 0);
        WA3W            : in     vl_logic_vector(3 downto 0);
        WA3E            : in     vl_logic_vector(3 downto 0);
        FowardAE        : out    vl_logic_vector(1 downto 0);
        FowardBE        : out    vl_logic_vector(1 downto 0);
        StallF          : out    vl_logic;
        StallD          : out    vl_logic;
        FlushD          : out    vl_logic;
        FlushE          : out    vl_logic
    );
end HazardUnit;
