# ☕ Java Quote Service Backend

A minimal Java backend for serving and storing motivational quotes, using Spark Java and SQLite.

---

## ✅ Directory Structure

quote-app/ └── backend/ ├── pom.xml └── src/ └── main/ └── java/ └── com/ └── example/ └── QuoteService.java



---

## 📦 pom.xml

Minimal working `pom.xml` with Spark, SQLite, and exec plugin configured:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>quote-service</artifactId>
  <version>1.0</version>

  <dependencies>
    <dependency>
      <groupId>com.sparkjava</groupId>
      <artifactId>spark-core</artifactId>
      <version>2.9.4</version>
    </dependency>
    <dependency>
      <groupId>org.xerial</groupId>
      <artifactId>sqlite-jdbc</artifactId>
      <version>3.43.2.1</version>
    </dependency>
    <dependency>
      <groupId>com.google.code.gson</groupId>
      <artifactId>gson</artifactId>
      <version>2.10.1</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.1.0</version>
        <executions>
          <execution>
            <goals>
              <goal>java</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <mainClass>com.example.QuoteService</mainClass>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>


```java

package com.example;

import static spark.Spark.*;

import com.google.gson.Gson;
import java.sql.*;
import java.util.HashMap;
import java.util.Map;

public class QuoteService {
    private static final String DB_URL = "jdbc:sqlite:quotes.db";
    private static final Gson gson = new Gson();

    public static void main(String[] args) {
        port(8080);
        initDatabase();

        get("/quote", (req, res) -> {
            Map<String, String> result = new HashMap<>();
            try (Connection conn = DriverManager.getConnection(DB_URL);
                 Statement stmt = conn.createStatement();
                 ResultSet rs = stmt.executeQuery("SELECT quote FROM quotes ORDER BY RANDOM() LIMIT 1")) {
                if (rs.next()) {
                    result.put("quote", rs.getString("quote"));
                } else {
                    result.put("quote", "No quotes available.");
                }
            } catch (SQLException e) {
                result.put("error", e.getMessage());
            }
            res.type("application/json");
            return gson.toJson(result);
        });

        post("/quote", (req, res) -> {
            Map<String, String> payload = gson.fromJson(req.body(), Map.class);
            Map<String, String> result = new HashMap<>();
            try (Connection conn = DriverManager.getConnection(DB_URL);
                 PreparedStatement pstmt = conn.prepareStatement("INSERT INTO quotes(quote) VALUES (?)")) {
                pstmt.setString(1, payload.get("quote"));
                pstmt.executeUpdate();
                result.put("status", "success");
            } catch (SQLException e) {
                result.put("error", e.getMessage());
            }
            res.type("application/json");
            return gson.toJson(result);
        });
    }

    private static void initDatabase() {
        try (Connection conn = DriverManager.getConnection(DB_URL);
             Statement stmt = conn.createStatement()) {
            stmt.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY AUTOINCREMENT, quote TEXT NOT NULL)");
        } catch (SQLException e) {
            System.err.println("DB init error: " + e.getMessage());
        }
    }
}


🛠️ How to Run
From the backend/ directory:

bash
Copy
Edit
mvn compile exec:java
💡 Ensure you have Java 17+ and Maven installed.

🧪 Test It
✅ Add a quote:
bash
Copy
Edit
curl -X POST http://localhost:8080/quote \
     -H "Content-Type: application/json" \
     -d "{\"quote\": \"The only way out is through.\"}"
✅ Get a random quote:
bash
Copy
Edit
curl http://localhost:8080/quote
