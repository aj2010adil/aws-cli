# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from awscli.testutils import BaseAWSCommandParamsTest


class TestDDB(BaseAWSCommandParamsTest):
    def test_no_command_specified(self):
        _, stderr, _ = self.run_cmd('ddb', expected_rc=255)
        expected = (
            "usage: aws [options] <command> <subcommand> "
            "[parameters]\naws: error: too few arguments"
        )
        self.assertIn(expected, stderr)