#!/usr/bin/env python3
"""
Test Script - Debug Output Validation
======================================

Purpose:
    Test the full pipeline with debug output enabled to validate
    all phase logging is working correctly.
    
Usage:
    conda activate squan
    cd tests/
    python test_debug_output.py
    
    Or from root:
    python tests/test_debug_output.py
    
Expected Output:
    Detailed logging from all 5 phases:
    - Phase 1: Input Phase
    - Phase 2: Schedule Phase
    - Phase 3: Transpile Phase
    - Phase 4: Execution Phase
    - Phase 5: Result Phase
"""

import sys
import os
# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flow.input.phase_input import ConcreteInputPhase
from flow.schedule.phase_schedule import ConcreteSchedulePhase
from flow.transpile.phase_transpile import ConcreteTranspilePhase
from flow.execution.execution_phase import ConcreteExecutionPhase
from flow.result.result_phase import ConcreteResultPhase
from flow.information.result_schedule import ResultOfSchedule

def main():
    """Run complete pipeline with debug output"""
    
    print("\n" + "="*70)
    print("QUANTUM SCHEDULING PIPELINE - DEBUG TEST")
    print("="*70)
    print("Testing all 5 phases with detailed logging enabled...")
    print("="*70 + "\n")
    
    # Initialize result container
    result_Schedule = ResultOfSchedule()
    
    try:
        # Phase 1: Input
        input_phase = ConcreteInputPhase()
        origin_job_info, machines, result_Schedule = input_phase.execute(result_Schedule)
        
        # Phase 2: Schedule
        schedule_phase = ConcreteSchedulePhase()
        scheduler_job, data, result_Schedule = schedule_phase.execute(
            origin_job_info, machines, result_Schedule
        )
        
        # Phase 3: Transpile
        transpile_phase = ConcreteTranspilePhase()
        scheduler_job, result_Schedule = transpile_phase.execute(
            scheduler_job, machines
        )
        
        # Phase 4: Execution
        execution_phase = ConcreteExecutionPhase()
        scheduler_job, utilization_permachine = execution_phase.execute(
            scheduler_job, machines, data
        )
        
        # Phase 5: Result
        result_phase = ConcreteResultPhase()
        final_result = result_phase.execute(
            scheduler_job, origin_job_info, data, utilization_permachine, result_Schedule
        )
        
        print("\n" + "="*70)
        print("DEBUG TEST COMPLETED SUCCESSFULLY")
        print("="*70)
        print("\nAll phases executed with debug output enabled.")
        print("Check the console output above for detailed logging.")
        print("="*70 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ ERROR: Pipeline execution failed!")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
