---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.55
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.33
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.13
      win_rate: 0.67
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.24
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.0
  - name: Breastplate of Valor
    pick_rate: 0.21
    win_rate: 0.78
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.29
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.0
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.17
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.75
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.67
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 1.0
  - name: Medallion
    pick_rate: 0.11
    win_rate: 0.0
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.36
    win_rate: 0.31
  - name: Bluestone Brooch
    pick_rate: 0.33
    win_rate: 0.67
  - name: Selflessness
    pick_rate: 0.09
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-08-13'
  god_win_rate: 0.4888888888888889
  god_matches_won: 22
  god_matches_played: 45
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Jotunn''s Revenge,
    Gluttonous Grimoire, The Crusher, Oni Hunter''s Garb, Shield Splitter, Shield
    of the Phoenix, Hydra''s Lament, Runeforged Hammer, Erosion, Eye of the Storm,
    Eye of Providence, Spectral Armor, Draconic Scale, Pharaoh''s Curse, Soul Gem,
    Golden Blade, Leviathan''s Hide, Death Metal, Midgardian Mail, Mantle Of Discord,
    Avenging Blade, Stone of Binding, Helm of Radiance, Shogun''s Ofuda, Damaru, Lernaean
    Bow, Magi''s Cloak, Yogi''s Necklace, Ancile, Screeching Gargoyle, Rod of Asclepius,
    Void Shield, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.18
      fit: 0.31
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.36
    Freya's Tears:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.5
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Rod of Asclepius, Chandra''s Grace,
    The Crusher, Oni Hunter''s Garb, Runeforged Hammer, Hydra''s Lament, Eye of the
    Storm, The Reaper, Shield Splitter, Erosion, Phoenix Feather, Eye of Providence,
    Spectral Armor, Pharaoh''s Curse, Blood-Bound Book, Draconic Scale, Bancroft''s
    Talon, Golden Blade, Leviathan''s Hide, Riptalon, Lifebinder, Avenging Blade,
    Midgardian Mail, Death Metal, Shogun''s Ofuda, Glorious Pridwen, Yogi''s Necklace,
    Damaru, Lernaean Bow, Helm of Radiance.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.38
    Freya's Tears:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Soul Gem, Kinetic
    Cuirass, Amanita Charm, Berserker''s Shield, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Spear of the Magus, Void Shield, Oni Hunter''s Garb, The
    Cosmic Horror, Hydra''s Lament, Void Stone, The Reaper, Shield of the Phoenix,
    Runeforged Hammer, Spear of Desolation, Shield Splitter, Riptalon, Obsidian Shard,
    Spectral Armor, Heartseeker, Erosion, Eye of the Storm, Pharaoh''s Curse, Eye
    of Providence, Silverbranch Bow, Draconic Scale, Death Metal, Golden Blade, Leviathan''s
    Hide, Helm of Radiance, Titan''s Bane, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.22
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.26
    Freya's Tears:
      total: 0.72
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The Crusher, Oni
    Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Hydra''s
    Lament, Shield of the Phoenix, Tyrfing, Runeforged Hammer, Spectral Armor, Erosion,
    Bracer of The Abyss, Shield Splitter, Eye of Providence, Eye of the Storm, Draconic
    Scale, Helm of Radiance, Leviathan''s Hide, Eros'' Bow, Yogi''s Necklace, Death
    Metal, Midgardian Mail, Dominance, Spear of the Magus, Mantle Of Discord, Bragi''s
    Harp, Stone of Binding, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.19
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.23
    Freya's Tears:
      total: 0.71
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.31
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Shield
    of the Phoenix, Kinetic Cuirass, Gluttonous Grimoire, Amanita Charm, Hydra''s
    Lament, Berserker''s Shield, Oni Hunter''s Garb, Chronos'' Pendant, Screeching
    Gargoyle, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s Shield,
    Erosion, Spectral Armor, Prophetic Cloak, Eye of Providence, Pharaoh''s Curse,
    Gem of Focus, Runeforged Hammer, Helm of Radiance, Shield Splitter, Draconic Scale,
    Totem of Death, Leviathan''s Hide, Eye of the Storm, Rod of Asclepius, Death Metal,
    Spear of the Magus, Arondight, Midgardian Mail, Jade Scepter, Mantle Of Discord,
    Stone of Binding, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.18
      fit: 0.48
    Breastplate of Valor:
      total: 0.67
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.28
    Freya's Tears:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.63
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Gluttonous Grimoire
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire, The
    Crusher, Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Hydra''s Lament,
    Soul Gem, Runeforged Hammer, Oni Hunter''s Garb, Shield Splitter, Golden Blade,
    Pharaoh''s Curse, Lernaean Bow, Shield of the Phoenix, Eye of the Storm, Death
    Metal, Spectral Armor, Erosion, Spear of the Magus, Eye of Providence, The Reaper,
    Damaru, Shogun''s Ofuda, Avenging Blade, The Cosmic Horror, Draconic Scale, Riptalon,
    Leviathan''s Hide, Helm of Radiance, Heartseeker, Midgardian Mail, Tekko-Kagi,
    Silverbranch Bow, Yogi''s Necklace, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.22
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.26
    Freya's Tears:
      total: 0.72
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Soul Gem, Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Spear
    of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, The Cosmic Horror,
    Runeforged Hammer, Helm of Radiance, Shield of the Phoenix, Shield Splitter, Spear
    of Desolation, Rod of Asclepius, Eye of the Storm, Spectral Armor, Erosion, Obsidian
    Shard, Jade Scepter, Pharaoh''s Curse, Eye of Providence, Chronos'' Pendant, Golden
    Blade, Draconic Scale, Blood-Bound Book, Damaru, Lernaean Bow, The Reaper, Leviathan''s
    Hide, Bancroft''s Talon, Ethereal Staff, Wish-Granting Pearl, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.18
      fit: 0.22
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.22
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.22
      fit: 0.26
    Freya's Tears:
      total: 0.72
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Jotunn''s Revenge, Gluttonous Grimoire, The Crusher, Oni Hunter''s Garb, Shield
    Splitter, Shield of the Phoenix, Hydra''s Lament, Runeforged Hammer, Erosion,
    Eye of the Storm, Eye of Providence, Spectral Armor, Draconic Scale, Pharaoh''s
    Curse, Soul Gem, Golden Blade, Leviathan''s Hide, Death Metal, Midgardian Mail,
    Mantle Of Discord, Avenging Blade, Stone of Binding, Helm of Radiance, Shogun''s
    Ofuda, Damaru, Lernaean Bow, Magi''s Cloak, Yogi''s Necklace, Ancile, Screeching
    Gargoyle, Rod of Asclepius, Void Shield, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.18
      fit: 0.31
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.22
      fit: 0.5
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
---
