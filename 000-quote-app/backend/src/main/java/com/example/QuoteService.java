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
