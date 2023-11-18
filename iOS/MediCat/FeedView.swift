//
//  FeedView.swift
//  MediCat
//
//  Created by Nikolas Psathakis on 18.11.23.
//

import SwiftUI

struct FeedView: View {
    @StateObject var viewModel = FeedViewModel()

    var body: some View {
        NavigationView {
            List(viewModel.items) { item in
                ParagraphView(item: item)
            }
            .navigationTitle("🫀HF Updates🫀")
        }
    }
}
