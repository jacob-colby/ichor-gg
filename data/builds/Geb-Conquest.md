---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.55
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.27
    win_rate: 0.54
    alternates:
    - name: Stampede
      pick_rate: 0.18
      win_rate: 0.62
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.3
    win_rate: 0.56
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.15
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.48
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.2
      win_rate: 0.55
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.58
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.59
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.66
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.61
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.71
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.72
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.69
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.38
  community_starters:
  - name: Selflessness
    pick_rate: 0.37
    win_rate: 0.47
  - name: Heroism
    pick_rate: 0.25
    win_rate: 0.63
  - name: Archmage's Gem
    pick_rate: 0.09
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-08-10'
  god_win_rate: 0.531578947368421
  god_matches_won: 303
  god_matches_played: 570
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Shifter''s Shield, Erosion, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Oni Hunter''s Garb, Spectral Armor, Gluttonous
    Grimoire, Mantle Of Discord, Stone of Binding, Leviathan''s Hide, Midgardian Mail,
    Magi''s Cloak, Gladiator''s Shield, Hussar''s Wings, Xibalban Effigy, Ancile,
    Void Shield, Hide of the Nemean Lion, Doublet of Binding, Screeching Gargoyle,
    Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.45
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.59
      pick: 0.25
      fit: 0.45
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.6
      pick: 0.19
      fit: 0.76
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.85
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace, Draconic Scale,
    Gluttonous Grimoire, Phoenix Feather, Rod of Asclepius, Spectral Armor, Soul Gem,
    Leviathan''s Hide, Midgardian Mail, Glorious Pridwen, Gladiator''s Shield, Ancile,
    Void Shield, Hide of the Nemean Lion, Mantle Of Discord, Doublet of Binding, Stone
    of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.42
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.94
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 1.0
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.19
      fit: 0.68
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.84
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Breastplate of Valor
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone
    of Binding, Screeching Gargoyle, Void Shield, Oni Hunter''s Garb, Spear of the
    Magus, Shield of the Phoenix, Void Stone, Shifter''s Shield, The Cosmic Horror,
    Erosion, Eye of Providence, Spectral Armor, Spear of Desolation, Draconic Scale,
    Obsidian Shard, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Magi''s
    Cloak, Helm of Radiance.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.48
      win: 0.59
      pick: 0.0
      fit: 0.78
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.28
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.25
      fit: 0.28
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.19
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s Garb,
    Shield of the Phoenix, Soul Gem, Spectral Armor, Shifter''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Leviathan''s Hide, Bracer of The Abyss, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Yogi''s Necklace, Helm of Radiance,
    Death Metal, Screeching Gargoyle, Magi''s Cloak, Bragi''s Harp, Ancile, Rod of
    Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.21
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.49
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.56
      win: 0.59
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.48
      efficiency: 0.49
      win: 0.59
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.59
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shield of the Phoenix, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Gluttonous Grimoire, Oni Hunter''s Garb, Screeching Gargoyle,
    Chronos'' Pendant, Gladiator''s Shield, Chandra''s Grace, Shifter''s Shield, Erosion,
    Spectral Armor, Eye of Providence, Spear of Desolation, Draconic Scale, Helm of
    Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail,
    Stone of Binding, Rod of Asclepius, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.5
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.59
      pick: 0.25
      fit: 0.5
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.57
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.63
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.19
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, The
    Crusher, Kinetic Cuirass, Gluttonous Grimoire, Amanita Charm, Hydra''s Lament,
    Shield Splitter, Oni Hunter''s Garb, Runeforged Hammer, Golden Blade, Pharaoh''s
    Curse, Soul Gem, Eye of the Storm, Lernaean Bow, Shield of the Phoenix, Shifter''s
    Shield, Erosion, Spectral Armor, Eye of Providence, Shogun''s Ofuda, Draconic
    Scale, The Reaper, Damaru, Death Metal, Avenging Blade, Spear of the Magus, Riptalon,
    Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Heartseeker,
    Tekko-Kagi, The Cosmic Horror, Silverbranch Bow, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.23
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Spear
    of the Magus, Oni Hunter''s Garb, Death Metal, Hydra''s Lament, The Cosmic Horror,
    Runeforged Hammer, Shield Splitter, Helm of Radiance, Shield of the Phoenix, Shifter''s
    Shield, Erosion, Spear of Desolation, Spectral Armor, Eye of the Storm, Rod of
    Asclepius, Eye of Providence, Pharaoh''s Curse, Obsidian Shard, Jade Scepter,
    Draconic Scale, Golden Blade, Chronos'' Pendant, Leviathan''s Hide, Blood-Bound
    Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.59
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Shifter''s Shield, Erosion,
    Eye of Providence, Shield of the Phoenix, Draconic Scale, Oni Hunter''s Garb,
    Spectral Armor, Gluttonous Grimoire, Mantle Of Discord, Stone of Binding, Leviathan''s
    Hide, Midgardian Mail, Magi''s Cloak, Gladiator''s Shield, Prophetic Cloak, Hussar''s
    Wings, Xibalban Effigy, Ancile, Void Shield, Hide of the Nemean Lion, Doublet
    of Binding, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.56
      pick: 0.41
      fit: 0.45
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.59
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.6
      pick: 0.19
      fit: 0.76
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.85
  starter: *id001
---
