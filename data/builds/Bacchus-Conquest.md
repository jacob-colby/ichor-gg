---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.36
    win_rate: 0.5
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.47
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.52
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.66
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.65
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.59
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.58
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.66
    alternates:
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.65
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Shield
      pick_rate: 0.06
      win_rate: 0.52
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.56
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.21
    win_rate: 0.53
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.44
  - name: Sundering Axe
    pick_rate: 0.14
    win_rate: 0.66
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-10'
  god_win_rate: 0.553050397877984
  god_matches_won: 417
  god_matches_played: 754
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Draconic Scale, Berserker''s
    Shield, Gluttonous Grimoire, Prophetic Cloak, Oni Hunter''s Garb, Erosion, Shield
    of the Phoenix, Eye of Providence, Spectral Armor, Jotunn''s Revenge, Pharaoh''s
    Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone
    of Binding, Midgardian Mail, The Crusher, Eye of the Storm, Shogun''s Ofuda, Helm
    of Radiance, Magi''s Cloak, Hydra''s Lament, Runeforged Hammer, Ancile, Gladiator''s
    Shield, Xibalban Effigy, Void Shield, Screeching Gargoyle, Doublet of Binding,
    Rod of Asclepius, Yogi''s Necklace, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.37
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.62
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.66
      pick: 0.11
      fit: 0.68
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Draconic Scale, Berserker''s Shield, Soul Gem, Gluttonous Grimoire, Rod of Asclepius,
    Oni Hunter''s Garb, Chandra''s Grace, Erosion, Eye of Providence, Phoenix Feather,
    Spectral Armor, Jotunn''s Revenge, Pharaoh''s Curse, Leviathan''s Hide, Blood-Bound
    Book, Bancroft''s Talon, Midgardian Mail, Lifebinder, Runeforged Hammer, Eye of
    the Storm, The Crusher, Glorious Pridwen, Shogun''s Ofuda, Shield Splitter, Riptalon,
    Gladiator''s Shield, Hydra''s Lament, Ancile, Yogi''s Necklace, Void Shield, Mantle
    Of Discord, The Reaper.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.76
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.54
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.66
      pick: 0.11
      fit: 0.66
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  flex_slots:
  - The Crusher
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass, Jotunn''s
    Revenge, The Crusher, Soul Gem, Amanita Charm, Draconic Scale, Berserker''s Shield,
    Stone of Binding, Screeching Gargoyle, Spear of the Magus, Void Shield, Oni Hunter''s
    Garb, The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear of Desolation,
    Avenging Blade, Erosion, Eye of Providence, Spectral Armor, Obsidian Shard, Riptalon,
    Pharaoh''s Curse, Silverbranch Bow, The Reaper, Shield Splitter, Hydra''s Lament,
    Leviathan''s Hide, Mantle Of Discord, Helm of Radiance, Midgardian Mail, Runeforged
    Hammer, Shogun''s Ofuda, Heartseeker, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.58
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.62
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.66
      pick: 0.11
      fit: 0.48
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire,
    Amanita Charm, Draconic Scale, Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge,
    Riptalon, The Crusher, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda,
    Shield of the Phoenix, Silverbranch Bow, Hydra''s Lament, Tyrfing, Runeforged
    Hammer, Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of
    The Abyss, Eye of the Storm, Helm of Radiance, Leviathan''s Hide, Midgardian Mail,
    Mantle Of Discord, Yogi''s Necklace, Death Metal, Stone of Binding, Eros'' Bow,
    Dominance, Spear of the Magus, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.47
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.34
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Jotunn''s
    Revenge, Prophetic Cloak, Shield of the Phoenix, Soul Gem, Amanita Charm, Draconic
    Scale, Gluttonous Grimoire, Berserker''s Shield, Hydra''s Lament, Oni Hunter''s
    Garb, Screeching Gargoyle, Chronos'' Pendant, The Crusher, Spear of Desolation,
    Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence,
    Pharaoh''s Curse, Shield Splitter, Runeforged Hammer, Helm of Radiance, Gem of
    Focus, Leviathan''s Hide, Eye of the Storm, Mantle Of Discord, Midgardian Mail,
    Rod of Asclepius, Stone of Binding, Spear of the Magus, Death Metal, Arondight,
    Jade Scepter, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.16
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.55
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.43
      win: 0.66
      pick: 0.11
      fit: 0.64
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge, Kinetic
    Cuirass, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Amanita Charm,
    Draconic Scale, Hydra''s Lament, Soul Gem, Oni Hunter''s Garb, Runeforged Hammer,
    Shield Splitter, Pharaoh''s Curse, Golden Blade, Shield of the Phoenix, Lernaean
    Bow, Eye of the Storm, Erosion, Spectral Armor, Death Metal, Eye of Providence,
    Spear of the Magus, Shogun''s Ofuda, The Reaper, Damaru, Avenging Blade, The Cosmic
    Horror, Riptalon, Leviathan''s Hide, Helm of Radiance, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Heartseeker, Silverbranch Bow, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  flex_slots:
  - The Crusher
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Freya''s Tears,
    Kinetic Cuirass, Jotunn''s Revenge, The Crusher, Amanita Charm, Draconic Scale,
    Soul Gem, Berserker''s Shield, Spear of the Magus, Oni Hunter''s Garb, Hydra''s
    Lament, Death Metal, The Cosmic Horror, Runeforged Hammer, Shield Splitter, Helm
    of Radiance, Shield of the Phoenix, Spear of Desolation, Erosion, Spectral Armor,
    Eye of the Storm, Rod of Asclepius, Eye of Providence, Pharaoh''s Curse, Obsidian
    Shard, Jade Scepter, Chronos'' Pendant, Golden Blade, Leviathan''s Hide, Blood-Bound
    Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.66
      pick: 0.11
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of the
    Phoenix, Eye of Providence, Draconic Scale, Spectral Armor, Jotunn''s Revenge,
    Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, The Crusher, Eye of the Storm, Shogun''s Ofuda,
    Helm of Radiance, Magi''s Cloak, Hydra''s Lament, Runeforged Hammer, Ancile, Gladiator''s
    Shield, Xibalban Effigy, Void Shield, Screeching Gargoyle, Prophetic Cloak, Doublet
    of Binding, Rod of Asclepius, Yogi''s Necklace, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.37
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.16
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.08
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.68
  starter: *id001
---
