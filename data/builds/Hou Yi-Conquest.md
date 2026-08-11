---
type: smite-build
god: Hou Yi
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Mark
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.59
  slot_order:
  - name: Tyrfing
    pick_rate: 0.44
    win_rate: 0.55
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.23
      win_rate: 0.52
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.5
  - name: Dagger of Frenzy
    pick_rate: 0.24
    win_rate: 0.54
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.16
      win_rate: 0.58
    - name: Toxic Blade
      pick_rate: 0.13
      win_rate: 0.5
  - name: Odysseus' Bow
    pick_rate: 0.18
    win_rate: 0.52
    alternates:
    - name: Dominance
      pick_rate: 0.17
      win_rate: 0.57
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.54
  - name: Silverbranch Bow
    pick_rate: 0.17
    win_rate: 0.54
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.58
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.53
  - name: Riptalon
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.61
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.61
  - name: Hunter's Bow
    pick_rate: 0.1
    win_rate: 0.49
    alternates:
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.52
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.6
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.37
    win_rate: 0.59
  - name: Gilded Arrow
    pick_rate: 0.2
    win_rate: 0.39
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/hou-yi/
  last_verified: '2026-08-10'
  god_win_rate: 0.530016447368421
  god_matches_won: 1289
  god_matches_played: 2432
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Death Metal
  - Dominance
  - Gluttonous Grimoire
  - Riptalon
  flex_slots:
  - Berserker's Shield
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Berserker''s Shield, Gluttonous Grimoire, Damaru, Lernaean
    Bow, Jotunn''s Revenge, The Crusher, Soul Gem, Golden Blade, Genji''s Guard, Hydra''s
    Lament, Bracer of The Abyss, Bragi''s Harp, Demon Blade, Pharaoh''s Curse, Nimble
    Ring, Breastplate of Valor, Runeforged Hammer, Tekko-Kagi, The Reaper, Blood-Bound
    Book, Bancroft''s Talon, Spear of the Magus, Shogun''s Ofuda, Kinetic Cuirass,
    Musashi''s Dual Swords, Amanita Charm, The Cosmic Horror, Eros'' Bow, Oni Hunter''s
    Garb, Eye of Providence, Rage, Freya''s Tears, Avenging Blade, Helm of Radiance,
    Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.28
    Tyrfing:
      total: 0.51
      efficiency: 0.46
      win: 0.55
      pick: 0.44
      fit: 0.56
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Dominance:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.28
      fit: 0.44
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Death Metal
  - Dominance
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Damaru, Gluttonous Grimoire, Berserker''s Shield, Jotunn''s
    Revenge, The Crusher, Lernaean Bow, Soul Gem, Genji''s Guard, Golden Blade, Hydra''s
    Lament, Demon Blade, Bracer of The Abyss, Bragi''s Harp, Pharaoh''s Curse, Breastplate
    of Valor, Runeforged Hammer, Nimble Ring, The Reaper, Tekko-Kagi, Blood-Bound
    Book, Bancroft''s Talon, Spear of the Magus, Musashi''s Dual Swords, Kinetic Cuirass,
    Shogun''s Ofuda, Amanita Charm, The Cosmic Horror, Oni Hunter''s Garb, Eye of
    Providence, Rage, Eros'' Bow, Freya''s Tears, Helm of Radiance, Avenging Blade,
    Chronos'' Pendant.'
  slot_scores:
    Tyrfing:
      total: 0.51
      efficiency: 0.46
      win: 0.55
      pick: 0.44
      fit: 0.53
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Dominance:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.43
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.28
      fit: 0.41
    Damaru:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.49
    Demon Blade:
      total: 0.47
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Dominance
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Dominance
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, Gluttonous Grimoire, Shield
    of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Genji''s Guard, Blood-Bound
    Book, Pharaoh''s Curse, Bancroft''s Talon, The Reaper, The Crusher, Jotunn''s
    Revenge, Oni Hunter''s Garb, Death Metal, Golden Blade, Chandra''s Grace, Breastplate
    of Valor, Damaru, Lernaean Bow, Shogun''s Ofuda, Runeforged Hammer, Phoenix Feather,
    Freya''s Tears, Spectral Armor, Hydra''s Lament, Shifter''s Shield, Umbral Link,
    Erosion, Lifebinder, Eye of Providence, Shield Splitter, Eye of the Storm, Bracer
    of The Abyss, Leviathan''s Hide, Draconic Scale, Yogi''s Necklace, Midgardian
    Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.14
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.46
    Dominance:
      total: 0.49
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.3
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.28
      fit: 0.58
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Dominance
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Soul Gem, Berserker''s
    Shield, Spear of the Magus, Death Metal, The Reaper, The Cosmic Horror, Damaru,
    Lernaean Bow, Tekko-Kagi, Genji''s Guard, Avenging Blade, Obsidian Shard, Hydra''s
    Lament, Spear of Desolation, Heartseeker, Golden Blade, Screeching Gargoyle, Breastplate
    of Valor, Bracer of The Abyss, Pharaoh''s Curse, Stone of Binding, Runeforged
    Hammer, Bragi''s Harp, Titan''s Bane, Doom Orb, The World Stone, Kinetic Cuirass,
    Void Shield, Dreamer''s Idol, Blood-Bound Book, Amanita Charm, Bancroft''s Talon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.5
      efficiency: 0.46
      win: 0.55
      pick: 0.44
      fit: 0.44
    Dominance:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.34
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.28
      fit: 0.6
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.54
      pick: 0.28
      fit: 0.52
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Berserker's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Gluttonous Grimoire, Death Metal,
    Lernaean Bow, The Crusher, Jotunn''s Revenge, Damaru, Genji''s Guard, Soul Gem,
    Hydra''s Lament, Bracer of The Abyss, Pharaoh''s Curse, Bragi''s Harp, Breastplate
    of Valor, Runeforged Hammer, Nimble Ring, Demon Blade, Spear of the Magus, Blood-Bound
    Book, Tekko-Kagi, Kinetic Cuirass, Shogun''s Ofuda, Bancroft''s Talon, The Reaper,
    Amanita Charm, Oni Hunter''s Garb, The Cosmic Horror, Eros'' Bow, Eye of Providence,
    Freya''s Tears, Helm of Radiance, Yogi''s Necklace, Musashi''s Dual Swords.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.57
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.26
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.55
      pick: 0.44
      fit: 0.67
    Dominance:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.4
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.28
      fit: 0.56
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.54
      pick: 0.28
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Genji''s
    Guard, Hydra''s Lament, Breastplate of Valor, Gluttonous Grimoire, Berserker''s
    Shield, Death Metal, Chronos'' Pendant, The Crusher, Freya''s Tears, Damaru, Spear
    of Desolation, Lernaean Bow, Shield of the Phoenix, Bracer of The Abyss, Gem of
    Focus, Golden Blade, Screeching Gargoyle, Spear of the Magus, Pharaoh''s Curse,
    Blood-Bound Book, Chandra''s Grace, Bancroft''s Talon, Arondight, Bragi''s Harp,
    Nimble Ring, The Cosmic Horror, Kinetic Cuirass, Runeforged Hammer, Amanita Charm,
    Oni Hunter''s Garb, Helm of Radiance, Eye of Providence, Shogun''s Ofuda, The
    Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.31
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.2
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Dominance
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, Death Metal, The Crusher, Berserker''s Shield, Genji''s Guard, Spear
    of the Magus, The Cosmic Horror, Bracer of The Abyss, Hydra''s Lament, Spear of
    Desolation, Damaru, Lernaean Bow, Breastplate of Valor, Blood-Bound Book, Bragi''s
    Harp, Bancroft''s Talon, Chronos'' Pendant, Obsidian Shard, Nimble Ring, Helm
    of Radiance, Golden Blade, The Reaper, Rod of Asclepius, Pharaoh''s Curse, Runeforged
    Hammer, Jade Scepter, Gem of Focus, Kinetic Cuirass, Doom Orb, The World Stone,
    Tekko-Kagi, Freya''s Tears, Amanita Charm, Dreamer''s Idol.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.5
    Dominance:
      total: 0.49
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.54
      pick: 0.28
      fit: 0.32
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Dominance
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Dominance
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Death Metal,
    Soul Gem, The Crusher, Jotunn''s Revenge, Berserker''s Shield, Damaru, Lernaean
    Bow, Spear of the Magus, The Cosmic Horror, Bracer of The Abyss, Bragi''s Harp,
    Genji''s Guard, Hydra''s Lament, Golden Blade, The Reaper, Blood-Bound Book, Bancroft''s
    Talon, Obsidian Shard, Nimble Ring, Spear of Desolation, Tekko-Kagi, Runeforged
    Hammer, Breastplate of Valor, Helm of Radiance, Pharaoh''s Curse, Chronos'' Pendant,
    Rod of Asclepius, Kinetic Cuirass, Heartseeker, Jade Scepter, Amanita Charm, Doom
    Orb, The World Stone, Oni Hunter''s Garb, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.5
      efficiency: 0.46
      win: 0.55
      pick: 0.44
      fit: 0.47
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Dominance:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Damaru
  flex_slots:
  - Lernaean Bow
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Death Metal, Berserker''s Shield, Gluttonous Grimoire,
    Damaru, Lernaean Bow, Jotunn''s Revenge, The Crusher, Soul Gem, Golden Blade,
    Genji''s Guard, Hydra''s Lament, Bracer of The Abyss, Bragi''s Harp, Demon Blade,
    Pharaoh''s Curse, Nimble Ring, Breastplate of Valor, Runeforged Hammer, Tekko-Kagi,
    The Reaper, Blood-Bound Book, Bancroft''s Talon, Spear of the Magus, Shogun''s
    Ofuda, Kinetic Cuirass, Musashi''s Dual Swords, Amanita Charm, The Cosmic Horror,
    Eros'' Bow, Oni Hunter''s Garb, Eye of Providence, Rage, Freya''s Tears, Avenging
    Blade, Helm of Radiance, Chronos'' Pendant.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.27
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.32
    Damaru:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
---
