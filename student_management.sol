// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Student_Management {
    struct Student {
        string name;
        uint256 age;
        string enrollmentStatus;
        uint256[] grades;
    }
    mapping(uint256 => Student) public students;
    uint256[] public studentIds;

    constructor(
        string memory _name,
        uint256 _age,
        string memory _enrollmentStatus,
        uint256[] memory _grades
    ) {
        students[1] = Student(_name, _age, _enrollmentStatus, _grades);

        studentIds.push(1);
    }

    function addStudent(
        string memory _name,
        uint256 _age,
        string memory _enrollmentStatus,
        uint256[] memory _grades
    ) public {
        uint256 newID = studentIds.length + 1;
        students[newID] = Student(_name, _age, _enrollmentStatus, _grades);

        studentIds.push(newID);
    }

    function updateStudentInfo(uint256 ID, string memory _enrollmentStatus)
        public
    {
        uint256 validity = 0;
        for (uint256 i = 0; i < studentIds.length; i++) {
            if (studentIds[i] == ID) {
                validity = 1;
            }
        }
        require(validity != 0, "Student does not exist!");
        students[ID].enrollmentStatus = _enrollmentStatus;
    }

    function getStudents(uint256 StudentID)
        public
        view
        returns (
            string memory,
            uint256,
            string memory,
            uint256[] memory
        )
    {
        uint256 validity = 0;
        for (uint256 i = 0; i < studentIds.length; i++) {
            if (studentIds[i] == StudentID) {
                validity = 1;
            }
        }
        require(validity != 0, "Student does not exist!");
        Student memory student = students[StudentID];

        return (
            student.name,
            student.age,
            student.enrollmentStatus,
            student.grades
        );
    }

    function updateStudentAge(uint256 ID, uint256 _age) public {
        uint256 validity = 0;
        for (uint256 i = 0; i < studentIds.length; i++) {
            if (studentIds[i] == ID) {
                validity = 1;
            }
        }
        require(validity != 0, "Student does not exist!");
        students[ID].age = _age;
    }
}
