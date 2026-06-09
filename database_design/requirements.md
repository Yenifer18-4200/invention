# Software Requirements Specification (SRS)

## 1. Introduction
This document defines the formal Functional and Non-Functional requirements for the **Virtual Store: Customer Order Management System**. It serves as the baseline for system evaluation, database validation, and architectural compliance for the SENA Software Analysis and Development portfolio.


## 2. System Scope
The application manages a localized backend environment capable of orchestrating user profiles, itemized product inventories, multi-product order transactions, and structured invoice generation using a lightweight, relational SQLite database architecture.


## 3. Functional Requirements (FR)
Functional requirements define the specific behaviors, calculations, data processing, and management tasks that the system must execute.

| Requirement ID | System Module | Description |
| :--- | :--- | :--- |
| **FR1** | User Management | The system shall allow the registration of new users, capturing distinct properties including Name, Email, Password, and System Role (`customer`, `admin`). |
| **FR2** | Inventory Ingestion | The system shall allow the registration of new products, establishing unique records containing Product Name, Unit Price, and Initial Stock Level. |
| **FR3** | Data Presentation | The system shall query and display comprehensive tabular catalogs of all registered users and available inventory metrics directly in the console interface. |
| **FR4** | Order Initialization | The system shall allow the creation of unique parent order headers, tracking the transaction date and establishing a Foreign Key link to the ordering User ID. |
| **FR5** | Transactional Line Items | The system shall allow multiple products to be linked to an active order via a junction table (`Order_items`), automatically validating stock availability before processing deductions. |
| **FR6** | State Management | The system shall allow an active order's lifecycle status to be dynamically updated between defined states: `Pending`, `Completed`, or `Cancelled`. |
| **FR7** | Business Reporting | The system shall cross-reference data across four distinct relational tables using optimized SQL `JOIN` statements to compile and display detailed, auto-calculated business invoices. |

## 4. Non-Functional Requirements (NFR)
Non-functional requirements specify system criteria, operational constraints, quality attributes, and performance boundaries.

### 🔒 NFR1: Data Security & Privacy
* The environment configuration shall isolate transactional database binaries (`*.db`) locally via project configuration rules (`.gitignore`), preventing data exposure on public remote repositories.
* The system shall ensure data integrity across tables by enforcing strict Foreign Key cascading constraints.

### 🎨 NFR2: Usability & Interface Design
* The system shall deliver a loop-driven command-line interface (CLI) that remains operational until explicitly terminated by the user.
* The system shall implement defensive input handling loops (`try/except`, `ValueError` trapping) to capture blank values or incorrect data types without crashing.

### ⚡ NFR3: Reliability & Performance
* The backend database engine shall complete relational queries, schema updates, and dynamic invoice generation pipelines within a execution window of under 2 seconds.
* The transaction modules shall utilize atomicity principles, ensuring partial failures invoke database rollbacks to prevent structural corruption.
